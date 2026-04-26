import {
  BrowserRouter,
  NavLink,
  Navigate,
  Outlet,
  Route,
  Routes,
} from "react-router-dom";
import { CategoriesPage } from "../pages/categories/CategoriesPage";
import { IngredientsPage } from "../pages/ingredients/IngredientsPage";
import { ProductDetailPage } from "../pages/products/ProductDetailPage";
import { ProductsPage } from "../pages/products/ProductsPage";

const linkBase =
  "flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium transition";

const AppLayout = () => {
  return (
    <div className="flex min-h-screen bg-zinc-950 text-white">
      {/* SIDEBAR */}
      <aside className="w-64 bg-zinc-900 border-r border-zinc-800 p-5 flex flex-col">
        <h2 className="text-xl font-bold mb-8">MiTiendita</h2>

        <nav className="flex flex-col gap-2">
          <NavLink
            to="/productos"
            className={({ isActive }) =>
              `${linkBase} ${
                isActive
                  ? "bg-emerald-500 text-white shadow-md"
                  : "text-gray-400 hover:bg-zinc-800"
              }`
            }
          >
            Productos
          </NavLink>

          <NavLink
            to="/categorias"
            className={({ isActive }) =>
              `${linkBase} ${
                isActive
                  ? "bg-emerald-500 text-white shadow-md"
                  : "text-gray-400 hover:bg-zinc-800"
              }`
            }
          >
            Categorías
          </NavLink>

          <NavLink
            to="/ingredientes"
            className={({ isActive }) =>
              `${linkBase} ${
                isActive
                  ? "bg-emerald-500 text-white shadow-md"
                  : "text-gray-400 hover:bg-zinc-800"
              }`
            }
          >
            Ingredientes
          </NavLink>
        </nav>

        {/* FOOTER SIDEBAR */}
        <div className="mt-auto text-xs text-gray-500 pt-6">Sistema Admin</div>
      </aside>

      {/* CONTENIDO */}
      <main className="flex-1 p-8">
        <Outlet />
      </main>
    </div>
  );
};

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route path="/" element={<Navigate to="/productos" replace />} />
          <Route path="/productos" element={<ProductsPage />} />
          <Route path="/productos/:id" element={<ProductDetailPage />} />
          <Route path="/categorias" element={<CategoriesPage />} />
          <Route path="/ingredientes" element={<IngredientsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};
