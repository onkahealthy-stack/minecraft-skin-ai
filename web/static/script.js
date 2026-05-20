// Minecraft Skin AI Generator - Frontend Script

const API_BASE = '/api';

// DOM Elements
const generateBtn = document.getElementById('generateBtn');
const randomBtn = document.getElementById('randomBtn');
const promptInput = document.getElementById('prompt');
const styleSelect = document.getElementById('style');
const skinsList = document.getElementById('skinsList');
const noSkins = document.getElementById('noSkins');

// Event Listeners
generateBtn.addEventListener('click', generateSkin);
randomBtn.addEventListener('click', randomSkin);

// Load initial data
loadSkins();

/**
 * Generate skin from prompt
 */
async function generateSkin() {
    const prompt = promptInput.value.trim();
    const style = styleSelect.value;

    if (!prompt) {
        alert('Пожалуйста, введите описание скина');
        return;
    }

    await callAPI('/generate', {
        prompt,
        style
    });
}

/**
 * Generate random skin
 */
async function randomSkin() {
    await callAPI('/random', {
        style: styleSelect.value
    });
}

/**
 * Call API endpoint
 */
async function callAPI(endpoint, data) {
    try {
        setLoading(true);
        const response = await fetch(`${API_BASE}${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Ошибка при генерации');
        }

        const result = await response.json();
        if (result.success) {
            promptInput.value = '';
            await loadSkins();
        }
    } catch (error) {
        alert(`Ошибка: ${error.message}`);
    } finally {
        setLoading(false);
    }
}

/**
 * Load all skins
 */
async function loadSkins() {
    try {
        const response = await fetch(`${API_BASE}/skins`);
        const skins = await response.json();

        if (skins.length === 0) {
            skinsList.innerHTML = '<p class="loading">Скины еще не созданы. Нажмите "Генерировать" для начала!</p>';
        } else {
            skinsList.innerHTML = skins.map(skin => `
                <div class="skin-card">
                    <div class="skin-preview">
                        <img src="/skins/${skin.id}.png" alt="${skin.prompt}">
                    </div>
                    <div class="skin-info">
                        <p>${skin.prompt.substring(0, 30)}...</p>
                        <div class="skin-style">${skin.style}</div>
                    </div>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading skins:', error);
    }
}

/**
 * Set loading state
 */
function setLoading(isLoading) {
    generateBtn.disabled = isLoading;
    randomBtn.disabled = isLoading;

    if (isLoading) {
        generateBtn.textContent = 'Генерирование... ⏳';
        randomBtn.textContent = 'Генерирование... ⏳';
    } else {
        generateBtn.textContent = 'Генерировать';
        randomBtn.textContent = 'Случайный';
    }
}
